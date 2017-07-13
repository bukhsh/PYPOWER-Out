def tol_pf_sol():
    """
    tolerences are given in (%) values"""
    v_tol = 10.0  # +- deviation from 1 p.u.
    pG_tol = 5.0
    qG_tol = 10.0
    br_tol = 10.0  # limit on apparent power
    return (v_tol, pG_tol, qG_tol, br_tol)