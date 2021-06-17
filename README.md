!! *WARNING: THIS IS NOT READY TO USE YET* !!

<div align="center">
  <h1 align="center">(ST)Ruckig</h1>
  <h3 align="center">
    Online Trajectory Generation. Real-time. Time-optimal. Jerk-constrained.<br/>
    "Full" port from C++ to Structured Text, TwinCAT 3.
  </h3>
</div>

This repository aims to port [pantor/ruckig](https://github.com/pantor/ruckig) to Structured Text to bring open-source powered Online
Trajectory Generation to TwinCAT 3. Please note, that while this port is aims to be a full port, it will probably never reach the performance 
of the original C++ code for the following reasons. 
- the original code uses templates and C++17 features to reduce load during runtime. 
- the codesys compiler , in contrast to C++ compilers, does not come with a lot of compile time optimizations. Even simple loop unwrapping optimizations are not performed - probably to make debugging easier (?)
- while some optimizations could be done by hand, I would rather have the port as close to the original as possible, only changing the architecture where it is required, because of limitiations of the programming language of the port.

If you are looking for best possible performance of Ruckig, I suggest you look into making pantor/ruckig a TwinCAT C++ module. However,
if you would like to use a library that is implemented in a IEC 61131-3 conform language, this port of pantor/ruckig might be for you.

## Progress report
*update 2021/0617: implemented cbrt since this is not available in vanilla structured text. The *general protection fault* exception was related to a call to SQRT(-1). While the C++ code seems to return NaN for this, TwinCAT instead brings this exception. It was a bit tricky to find, because the debugger stopped at a different location for some reason. Tried to run a simple trajectory with only 1 degree of freedom the calculated profile looked fine, but there is much more manual testing required and ofc. implementing the unittests from the original code.*

*update 2021/06/16: the port is not nearly finished yet. While most of the code has already been "translated" to structured text, the process was ... intense - It took me like 10 hours in one sitting... it was a lot of code that I had to "translate" manually and I wasnt always as concentrated as I should have been so... there are a lot of mistakes that will cause exceptions. And there is one specific "general protection fault" I do not understand at the moment. Also, some passages still require work. For instance, during "translating" I did not feel like implementing a quicksort algo used in the original code.*

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
