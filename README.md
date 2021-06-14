#ruckig TwinCAT port

This repository aims to port [pantor/ruckig](https://github.com/pantor/ruckig) to TwinCAT


- [ ] Crude initial port of source code
  - [ ] include/ruckig
    - [x] block.hpp
    - [x] brake.hpp
    - [x] input_parameters.hpp
    - [x] output_parameters.hpp
    - [ ] position.hpp
    - [x] profile.hpp      
    - [ ] roots.hpp
    - [ ] ruckig.hpp
    - [ ] trajectory.hpp
    - [ ] velocity.hpp
  - [ ] src
    - [x] brake.cpp
    - [ ] position-step1.cpp
    - [ ] position-step2.cpp
    - [ ] velocity-step1.cpp
    - [ ] velocity-step2.cpp
- [ ] Check source code for obvious copy & paste errors that may have occured during the port
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
- [ ] The original code is rather functional, which TwinCAT ST doesn't benefit from a lot, rewrite to OOP where needed
- [ ] Manual testing
- [ ] Initial commit
- [ ] Implement unit tests with TcUnit-Runner or use TcUnit-Wrapper to put aside this dependency
    - [ ] otg-test.cpp - for string this should be sufficient
    - [ ] otg-benchmark.cpp - implement test to check for regressions and test overall performance on codesys compiler 
    - [ ] run unit tests to find more issues that sneaked in while porting
- [ ] Code cleanup and optimize performance, some parts have to be change to be faster in twincat, we do not have the power of a cpp compiler :-(
- [ ] examples
  - [ ] position.cpp
- [ ] Documentation
