#struckig

This repository aims to port [pantor/ruckig](https://github.com/pantor/ruckig) to Structured Text (TwinCAT)


- [x] Crude initial port of source code
  - [x] include/ruckig
    - [x] block.hpp
    - [x] brake.hpp
    - [x] input_parameters.hpp
    - [x] output_parameters.hpp
    - [x] position.hpp
    - [x] profile.hpp      
    - [x] roots.hpp
    - [x] ruckig.hpp
    - [x] trajectory.hpp
    - [x] velocity.hpp
  - [x] src
    - [x] brake.cpp
    - [x] position-step1.cpp
    - [x] position-step2.cpp
    - [x] velocity-step1.cpp
    - [x] velocity-step2.cpp
- [ ] Check source code for obvious copy & paste errors that may have occured during the port
- [ ] Manual testing
- [ ] Initial commit
- [ ] Implement unit tests with TcUnit-Runner or use TcUnit-Wrapper to put aside this dependency
    - [ ] otg-test.cpp - this should be sufficient
    - [ ] otg-benchmark.cpp - implement test to check for regressions and test overall performance on codesys compiler 
    - [ ] run unit tests to find more issues that sneaked in while porting
- [ ] The original code is rather functional, which TwinCAT ST doesn't benefit from a lot, rewrite to OOP where needed
- [ ] Code cleanup and optimize performance, some parts have to be change to be faster in twincat, we do not have the power of a cpp compiler :-(
- [ ] examples
  - [ ] position.cpp
- [ ] Documentation
