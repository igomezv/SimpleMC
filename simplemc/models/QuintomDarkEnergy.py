## This is Quintom DE cosmology

from simplemc.models.LCDMCosmology import LCDMCosmology
from simplemc.cosmo.paramDefs import *
from scipy.interpolate import interp1d
from scipy.integrate import odeint
from scipy.optimize import ridder, minimize_scalar
import numpy as np


class QuintomDarkEnergy(LCDMCosmology):
    def __init__(self, model='quad', vary_coupling=False, vary_Ok=False, vary_iniphi=False):

        """
        It better to start the chains at masses equal one, othewise may take much longer.
        """

        self.model = model

        self.coupling = 0 if (not vary_coupling) else coupling_par.value
        self.vary_iniphi = vary_iniphi
        self.vary_coupling = vary_coupling
        self.vary_Ok = vary_Ok
        self.iniphi = 0
        self.Ok = Ok_par.value

        self.zvals = np.linspace(0, 3, 100)
        self.lna = np.linspace(-10, 0, 500)
        self.z = np.exp(-self.lna) - 1.

        #whether we rather printing all
        self.chatty = False

        self.Ol = 0
        self.alphaphi  = alphaphi_par.value
        self.alphapsi  = alphapsi_par.value

        LCDMCosmology.__init__(self, mnu=0)

        self.updateParams([])


    # Free parameters. We add Ok on top of LCDM ones (we inherit LCDM).
    def freeParameters(self):
        l = LCDMCosmology.freeParameters(self)
        l.append(alphaphi_par)
        l.append(alphapsi_par)
        if self.vary_iniphi: l.append(iniphi_par)
        if self.vary_coupling: l.append(coupling_par)
        if self.vary_Ok: l.append(Ok_par)
        return l


    def updateParams(self, pars):
        ok = LCDMCosmology.updateParams(self, pars)
        if not ok:
            return False

        for p in pars:
            if p.name  == "alphaphi":
                self.alphaphi = p.value
            elif p.name == "alphapsi":
                self.alphapsi = p.value
            elif p.name == "iniphi":
                self.iniphi = p.value
            elif p.name == 'beta':
                self.coupling = p.value
            elif p.name == "Ok":
                self.Ok = p.value
                self.setCurvature(self.Ok)
                if (abs(self.Ok) > 1.0):
                    return False


        # Searches initial conditions and stores the Hubble function.
        if self.chatty:
            print('-'*10)
            print ('alpha_phi={}, alpha_psi={}, coupling={}'.format(self.alphaphi, self.alphapsi, self.coupling))

        # Main method.
        self.initialize()

        return True


    def sf_potential(self, phi, psi, select=0):
        """
        Scalar field potentials for quintom-like models.

        params = (alpha_phi, alpha_psi, beta)
            alpha_phi: slope/curvature parameter for phi
            alpha_psi: slope/curvature parameter for psi
            beta: interaction strength between phi and psi

        select:
            0     -> return potential V
            'phi' -> return dV/dphi
            'psi' -> return dV/dpsi

        model:
            'quad'     -> Quadratic potential with quartic interaction
            'rp'       -> Ratra–Peebles (inverse power-law) potential
            'hilltop'  -> Hilltop (polynomial, p=4 by default)
            'hillcos'  -> Hilltop cosinoidal (PNGB-like) potential
            'expsum'   -> Sum of exponentials with interaction
            'expprod'  -> Product exponential with interaction

        Notes on typical parameters (from the literature, as guidelines):
            - Quadratic:
                alpha_phi=1e-2, alpha_psi=1e-2, beta=1e-3
            - Ratra–Peebles:
                alpha_phi=2, alpha_psi=2, beta=0.1
            - Hilltop (default p=4):
                alpha_phi=1e-3, alpha_psi=1e-3, beta=1e-2
                p=2 -> sharper hilltop (parabolic)
                p=4 -> flatter hilltop (common choice)
            - Hillcos (PNGB):
                alpha_phi=1/f, alpha_psi=1/f with f ~ 0.1–1 M_Pl
                e.g. f=0.5 M_Pl -> alpha_phi=2, alpha_psi=2
                beta=0.1
            - Expsum / Expprod:
                alpha_phi=1, alpha_psi=1, beta=0.1
            - V0:
                for dark energy, V0 ~ 1e-120 (in reduced Planck units)
                for toy models/tests, set V0=1.0
        """
        # alpha_phi, alpha_psi, beta = params
        V0 = 1.0  # default energy scale (adjust as needed)

        if self.model == 'quad':
            # Quadratic potential with quartic interaction
            if select == 0:
                return 0.5*(self.alphaphi*phi)**2 + 0.5*(self.alphapsi*psi)**2 + self.coupling*(phi*psi)**2
            elif select == 'phi':
                return self.alphaphi**2 * phi + 2*self.coupling*phi*psi**2
            elif select == 'psi':
                return self.alphapsi**2 * psi + 2*self.coupling*psi*phi**2

        elif self.model == 'rp':
            # Ratra–Peebles inverse power-law potential
            if select == 0:
                return V0*(phi**(-self.alphaphi) + psi**(-self.alphapsi) + self.coupling*(phi*psi)**(-(self.alphaphi+self.alphapsi)/2))
            elif select == 'phi':
                return -V0*(self.alphaphi*phi**(-self.alphaphi-1) + self.coupling*((self.alphaphi+self.alphapsi)/2)*phi**(-(self.alphaphi/2+1))*psi**(-self.alphapsi/2))
            elif select == 'psi':
                return -V0*(self.alphapsi*psi**(-self.alphapsi-1) + self.coupling*((self.alphaphi+self.alphapsi)/2)*psi**(-(self.alphapsi/2+1))*phi**(-self.alphaphi/2))

        elif self.model == 'hilltop':
            # Hilltop polynomial potential (default p=4)
            p = 4
            if select == 0:
                return V0*(1 - self.alphaphi*phi**p - self.alphapsi*psi**p - self.coupling*(phi*psi)**(p//2))
            elif select == 'phi':
                return -V0*(self.alphaphi*p*phi**(p-1) + self.coupling*(p//2)*phi**(p//2-1)*psi**(p//2))
            elif select == 'psi':
                return -V0*(self.alphapsi*p*psi**(p-1) + self.coupling*(p//2)*psi**(p//2-1)*phi**(p//2))

        elif self.model == 'hillcos':
            # Hilltop cosinoidal potential (PNGB-like)
            c_phi = np.cos(self.alphaphi*phi); s_phi = np.sin(self.alphaphi*phi)
            c_psi = np.cos(self.alphapsi*psi); s_psi = np.sin(self.alphapsi*psi)
            if select == 0:
                return V0*(1 - c_phi - c_psi - self.coupling*c_phi*c_psi)
            elif select == 'phi':
                return V0*self.alphaphi*s_phi*(1 + self.coupling*c_psi)
            elif select == 'psi':
                return V0*self.alphapsi*s_psi*(1 + self.coupling*c_phi)

        elif self.model == 'expsum':
            # Sum of exponentials with quadratic interaction
            e_phi  = np.exp(-self.alphaphi*phi)
            e_psi  = np.exp(-self.alphapsi*psi)
            if select == 0:
                return V0*(e_phi + e_psi)*(1 + self.coupling*(phi*psi)**2)
            elif select == 'phi':
                return V0*(-self.alphaphi*e_phi*(1 + self.coupling*(phi*psi)**2) + (e_phi+e_psi)*(2*self.coupling*phi*psi**2))
            elif select == 'psi':
                return V0*(-self.alphapsi*e_psi*(1 + self.coupling*(phi*psi)**2) + (e_phi+e_psi)*(2*self.coupling*psi*phi**2))

        elif self.model == 'expprod':
            # Product exponential with quadratic interaction
            e_prod = np.exp(-self.alphaphi*phi - self.alphapsi*psi)
            if select == 0:
                return V0*e_prod*(1 + self.coupling*(phi*psi)**2)
            elif select == 'phi':
                return e_prod*(-self.alphaphi*(1 + self.coupling*(phi*psi)**2) + 2*self.coupling*phi*psi**2)
            elif select == 'psi':
                return e_prod*(-self.alphapsi*(1 + self.coupling*(phi*psi)**2) + 2*self.coupling*psi*phi**2)

        else:
            raise ValueError(f"Unknown potential model: {self.model}")

        raise ValueError("select must be 0, 'phi', or 'psi'")


    def sf_rho(self, variables):
        """ Computes the density for the scalar field. """
        phi, x_phi, psi, x_psi = variables
        sf_rho = x_phi**2 - x_psi**2 + self.sf_potential(phi, psi, 0)/(3*self.h**2)
        return sf_rho


    def hubble(self, lna, variables=None, use_sf=True):
        """
        Computes the Hubble function for either a scalar-field or cosmological constant.

        Parameters
        ----------
        lna : array
            Interval of scale factor.
        variables : list , optional
            Array [phi, dotPhi, psi, dotPhi]. Defaults to ``None`` or LCDM model.
        use_sf : Boolean , optional
            Defaults to ``True`` or SFDE model, otherwise use LCDM.

        Returns
        -------
        hubble : array
            The ``hubble`` function value at the range ``lna``.

        """
        if use_sf:
            omega_de = self.sf_rho(variables)
        else:
            omega_de = 1.0 - self.Ocb - self.Ok - self.Omrad

        a = np.exp(lna)
        hubble = self.h*np.sqrt(self.Omrad/a**4 + self.Ocb/a**3 + self.Ok/a**2 + omega_de)
        return hubble


    def right_hand_side(self, variables, lna):
        """ Right hand side of the dynamical system. """

        factor = np.sqrt(6)*self.h

        # Compute hubble function.
        Hub  = self.hubble(lna, variables=variables)

        phi, x_phi, psi, x_psi = variables

        # Right hand side of the dynamical system.
        rhs = [factor*x_phi/Hub,
            -3*x_phi -self.sf_potential(phi, psi, 'phi')/(factor*Hub),
            factor*x_psi/Hub,
            -3*x_psi +self.sf_potential(phi, psi, 'psi')/(factor*Hub)]
        return rhs


    def solve_eqns(self, y0):
        """
        Input initial conditions for [phi, dotPhi, psi, dotPhi] and returns
        the solution of the Klein-Gordon equations.
        """
        # solution = odeint(self.right_hand_side, y0, self.lna, h0=1E-10)
        solution = odeint(
            lambda y, t: self.right_hand_side(y, t),
            y0,
            self.lna,
            h0=1e-10
        )
        return solution


    def compute_omega_de(self, ini_guess):
        """
        Given an guess for the initial condition of the field
        return the solution (if any) of the Klein-Gordon equation.
        """
        if self.alphaphi and (self.alphapsi == 0) and (self.coupling == 0):
            phi_ini, psi_ini = 10**ini_guess, 0
        elif self.alphapsi and (self.alphaphi == 0) and (self.coupling == 0):
            phi_ini, psi_ini = 0, 10**ini_guess
        else:
            if self.iniphi:
                phi_ini, psi_ini = 10**ini_guess, self.iniphi
            else:
                phi_ini, psi_ini = 10**ini_guess, 10**ini_guess

        # Find the solution for such a guess.
        solution = self.solve_eqns([phi_ini, 0.0, psi_ini, 0.0])

        # Solution at a=1.
        sf_rho0 = self.sf_rho(solution[-1])
        omega_de = sf_rho0*(self.h/self.hubble(self.lna[-1], solution[-1]))**2

        tolerance = (1 - self.Omrad - self.Ocb) - omega_de
        return solution.T, tolerance


    def find_initial_phi(self, low_guess=-2, high_guess=3, tolerance=5E-3):
        """Find initial phi with Ridder so that Ω_DE(today) matches observations."""
        def F(x):
            # objective: Omega_obs - Omega_model(x)
            _, tol = self.compute_omega_de(x)
            if self.chatty:
                print(f'-done- phi_0={x}, error={tol}')
            return tol

        # 1) Try Ridder (requires sign change, but faster than bisection)
        try:
            mid = ridder(F, low_guess, high_guess, xtol=tolerance, rtol=0.0, maxiter=200)
            solution, tol = self.compute_omega_de(mid)
            if self.chatty:
                print(f'-done- phi_0={mid}, error={tol}')
            return mid, solution
        except ValueError:
            pass  # no sign change or solver failed

        # 2) Fallback: bounded minimization of |F| within [low, high]
        res = minimize_scalar(lambda x: abs(F(x)),
                            bounds=(low_guess, high_guess),
                            method='bounded',
                            options={'xatol': tolerance})
        mid = float(res.x)
        solution, tol = self.compute_omega_de(mid)

        if abs(tol) < tolerance:
            if self.chatty:
                print(f'-done- phi_0={mid}, error={tol} (min |F|)')
            return mid, solution

        # 3) Final classification (LCDM / no-solution), no `self`
        grad = np.abs(np.gradient(self.sf_rho(solution))).max()
        mid = -1 if grad < 1.0e-2 else 0
        if self.chatty:
            print('looks a lot like LCDM' if mid == -1 else '-- No solution found!')
        return mid, solution


    def initialize(self):
        """
        Main method that searches the initial conditions and computes [phi, xPhi, psi, xPsi]
        for a given scalar field potential.
        """
        high_guess = 2 if self.coupling >0 else 1
        self.phi_ini, self.solution = self.find_initial_phi(-2, high_guess)

        if self.phi_ini == 0:
            # Solution couldn't be found, then reject that point.
            Hub = np.zeros_like(self.lna, dtype=float)
        elif self.phi_ini == -1:
            # Solution couldn't be found, but it is very close to the cosmological constant.
            Hub = self.hubble(self.lna, use_sf=False)
        else:
            # Solution found.
            Hub = self.hubble(self.lna, variables=self.solution, use_sf=True)

        self.sf_hubble = interp1d(self.lna, Hub, bounds_error=False, fill_value='extrapolate')
        return True


    def RHSquared_a(self, a):
        """ This is relative hsquared as a function of a, i.e. H(z)^2/H(z=0)^2. """

        self.initialize()

        if (1./a-1 < self.zvals[-1]):
            hubble_a = self.sf_hubble(np.log(a))
        else:
            hubble_a = self.hubble(np.log(a), use_sf=False)
        return (hubble_a/self.h)**2


    #-------------------------
    # External methods useful for plotting or testing.
    def logatoz(self, func):
        # change function from lna to z
        tmp     = interp1d(self.lna, func)
        functmp = tmp(self.lna)
        return np.interp(self.zvals, self.z[::-1], functmp[::-1])


    def Hubble_a(self, a):
        hubble = 100*self.sf_hubble(np.log(a))
        return hubble


    def sf_eos(self, variables):
        phi, dot_phi, psi, dot_psi = variables

        w1 = dot_phi**2 - dot_psi**2 - self.sf_potential(phi, psi, 0)/(3*self.h**2)
        w2 = dot_phi**2 - dot_psi**2 + self.sf_potential(phi, psi, 0)/(3*self.h**2)
        return  w1/w2


    def call_functions(self):
        if self.phi_ini == 0:
            w_eos = np.zeros(len(self.lna))
        elif self.phi_ini == -1:
            w_eos = -1*np.ones(len(self.lna))
        else:
            w_eos = self.sf_eos(self.solution)

        self.w_eos = interp1d(self.lna, w_eos)
        return True


    def w_de(self, a):
        lna = np.log(a)
        return self.w_eos(lna)





