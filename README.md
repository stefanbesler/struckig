#ruckig TwinCAT port

This repository aims to port [pantor/ruckig](https://github.com/pantor/ruckig) to TwinCAT


- [ ] Port source code
  - [ ] include/ruckig
    - [ ] block.hpp
    - [ ] brake.hpp
    - [ ] input_parameters.hpp
    - [ ] output_parameters.hpp
    - [ ] position.hpp
    - [ ] profile.hpp      
    - [ ] (reflexxes_comparision.hpp) - no need
    - [ ] roots.hpp
    - [ ] ruckig.hpp
    - [ ] trajectory.hpp
    - [ ] velocity.hpp
  - [ ] src
    - [ ] brake.cpp
    - [ ] position-step1.cpp
    - [ ] position-step2.cpp
    - [ ] (python.cpp) - no need
    - [ ] velocity-step1.cpp
    - [ ] velocity-step2.cpp
 - [ ] test
    - [ ] otg-test.cpp - for string this should be sufficient
    - [ ] otg-benchmark.cpp - implement test to check for regressions and test overall performance on codesys compiler
- [ ] Manual testing
- [ ] Implement unit tests with TcUnit-Runner or use TcUnit-Wrapper to put aside this dependency
     - [ ] run unit test
- [ ] Code cleanup and optimize performance, some parts have to be change to be faster in twincat, we do not have the power of a cpp compiler :-(
- [ ] examples
  - [ ] position.cpp
- [ ] Documentation
