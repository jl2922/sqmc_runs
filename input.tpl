2726516565436524 1346563466354361   irand_seed
2000   1000    10  0                nstep,nblk,nblk_eq,ipr
50 100000 1000000  w_abs_gen_begin, w_abs_gen_target, MWALK
1. 0.                               tau_multiplier, tau
1.0   0.0                           reweight_factor_inv_max_multiplier, reweight_factor_inv_max
100. -19. 0.5                       population_control_expon, e_trial_initial,min_wt
fast_heatbath 0 1.  1 1                   proposal_method, importance_sampling, r_initiator, initiator_power, initiator_rescale_power
hci                                 run_type
{{eps1}}    {{eps2}}  0.0002 1      min_elem, pt_eps, target_error
.false.
.false. f                           semistoch, use_exp_proj
'heg' 0                             hamiltonian_type,ipr
3                                   n_dim
0.5                                 r_s
38 19                               n_elec n_up
{{cutoff}} 1.0  1                   cutoff_radius, cut_off_radius_trial_wf, nsym_uniq_det_trial_wf
1                                   trial_wf_iters
81 81                               norb_trial_wf
1 10                                 n_initiators_trial_wf
1 10000                           n_truncate_trial_wf
0                                   diagonalize ham
