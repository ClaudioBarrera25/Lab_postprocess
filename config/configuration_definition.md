* lamb: [500,532,660,810] Lambdas of measures
* load_SIF: read sif data
* load_calib: load calibration images.
* side: Image side   0:left; 1:right
* AUTOalfa: Alpha parameter method   0:constant,   1:automatic
* alfa_o: 3e-6    # If Alpha regul. constante
* E_ref: Absorption function Model    1:Chang; 2:Jérôme Yon; 3:Krishnan
* rho_sa: scatering factor  0.16 (Sneling at 450 nm)
* smooth_tau: apply vertical smooth for transmissivity field
* plot_FIG: plot figures results, 1 or 0
* save_data: save_computed_fv_data_and_figures, 1 or 0
* activate_MC: Apply MC
* N_int:  Numero de iteraciones MC, 75 se demoran al menos 6h
* h_px = 600     # Select an height for procedure verification in px
* #Self_abs = 0    #
* lim_fv =0.3e-6
