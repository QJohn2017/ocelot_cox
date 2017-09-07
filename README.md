# Module for the particle tracker code <cite>[OCELOT]</cite>
## Modeling the broad spectra (LPA) beams in the COXINEL-like beamlines

### CONTAINS:
- beam generators for simple and sliced beams
- tools for:
  - beamline object creation
  - simulation running
  - 1st order sliced beam alignment
- beam diagnostics tool (for *make_shot* method))
- *slit* particle selection method
- tuning tool for super-matching of the beamline (object)
- printout of some S2I matricies coefficients
- beam export to <cite>[CHIMERA]</cite> for FEL, SR, PIC or SC simulations

### TODO:
- 2nd order sliced beam alignment
- space charge modeling of sliced beams
- beam diags treatment tools (collect and plot)

## Attribution
This softwre is developed and supported by <cite>[Igor A Andriyash]</cite>

Special thanks to 
- <cite>[Sergey Tomin]</cite> for advices and code pieces 
- <cite>[Alexandre Loulergue]</cite> for advices and help with benchmarking
- <cite>[Martin Khojoyan]</cite> for help with benchmarking

[OCELOT]:https://github.com/hightower8083/chimera
[CHIMERA]:https://github.com/iagapov/ocelot
[Igor A Andriyash]:mailto:igor.andriyash@gmail.com
[Sergey Tomin]:https://github.com/sergey-tomin
[Alexandre Loulergue]:mailto:alexandre.loulergue@synchrotron-soleil.fr
[Martin Khojoyan]:mailto:martinkh@mail.ru
