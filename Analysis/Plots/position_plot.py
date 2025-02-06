from Position_Plots import cod_position_plotter

cod_position_plotter.plot_beam_from_ascii_file('../Output/pos_210.cod', False, True, 15, show_reference=False)
cod_position_plotter.plot_beam_from_ascii_file('../Output/pos_repulsion.cod', False, True, 15, show_reference=False)

cod_position_plotter.plot_beam_from_ascii_file('../Output/positions.cod', False, True, 15, 2)
cod_position_plotter.plot_beam_from_ascii_file('../Output/pos_forward.cod', False, True, 15, 2, False)
