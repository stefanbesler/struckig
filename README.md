!! *WARNING: THIS IS NOT READY TO USE YET* !!

<div align="center">
  <h1 align="center">(ST)Ruckig</h1>
  <h3 align="center">
    Online Trajectory Generation. Real-time. Time-optimal. Jerk-constrained.<br/>
    "Full" port from C++ to Structured Text, TwinCAT 3.
  </h3>
</div>

This repository aims to port [pantor/ruckig](https://github.com/pantor/ruckig) to Structured Text to bring open-source powered Online
Trajectory Generation to TwinCAT 3. Please note, that while this port aims to be a full port, it will probably never reach the performance 
of the original C++ code for the following reasons. 
- the original code uses templates and C++17 features to reduce load during runtime. 
- the codesys compiler , in contrast to C++ compilers, does not come with a lot of compile time optimizations. Even simple loop unwrapping optimizations are not performed - probably to make debugging easier (?)
- while some optimizations could be done by hand, I would rather have the port as close to the original as possible, only changing the architecture where it is required, because of limitiations of the programming language of the port.

If you are looking for best possible performance of Ruckig, I suggest you look into making pantor/ruckig a TwinCAT C++ module. However,
if you would like to use a library that is implemented in a IEC 61131-3 conform language, this port of pantor/ruckig might be for you.

## Progress report
*update 2021/07/23: today I was in the mood to dig a bit deeper into some of the failed tests. I managed to fix the code to get to 14/18 successful tests. There was a bug regarding synchronization... There are still a lot of unittests missing that are implemented in ruckig. However, before porting those, I want to get to 18/18.

*update 2021/06/19: I am busy with other things at the moment so not so much progress on the code. I only had time to port one of the test cases (*known*) from otg-test.cpp. The results are *meh*, after some div0 exceptions fixes the result are 11/18 successful 3 tests can't find and profile and therefore fail, 2 tests fail because of precision (i.e. expected: 1.4939456041s, actual: 1.4937969582275) and another fails miserably, returning >1.8s instead of 8.9s).
Synchronization is still set to none for all test cases, I didn't look much into PositionStep2 so far - this code segment still causes exceptions.*

*update 2021/06/18: fixed some issues that showed up during manual testing. Simple profiles without synchronizations now seem to work. There might however still be some exceptions. Twincat is less forgiving about SSE2 exceptions, e.g. I do not know to turn them off explictly for a library - hence, there are some checks that have to be added to various methods. To find all related bugs more reliable, I will implement unittests during the next week.*

*update 2021/06/17: implemented cbrt since this is not available in vanilla structured text. The *general protection fault* exception was related to a call to SQRT(-1). While the C++ code seems to return NaN for this, TwinCAT instead brings this exception. It was a bit tricky to find, because the debugger stopped at a different location for some reason. Tried to run a simple trajectory with only 1 degree of freedom the calculated profile looked fine, but there is much more manual testing required and ofc. implementing the unittests from the original code.*

*update 2021/06/16: the port is not nearly finished yet. While most of the code has already been "translated" to structured text, the process was ... intense - It took me like 10 hours in one sitting... it was a lot of code that I had to "translate" manually and I wasnt always as concentrated as I should have been so... there are a lot of mistakes that will cause exceptions. And there is one specific "general protection fault" I do not understand at the moment. Also, some passages still require work. For instance, during "translating" I did not feel like implementing a quicksort algo used in the original code.*

- [x] Crude initial port of source code
- [ ] Check source code for obvious copy & paste errors that may have occured during the port
- [ ] Manual testing
- [x] Initial commit
- [ ] Implement unit tests with TcUnit-Runner or use TcUnit-Wrapper to put aside this dependency
    - [ ] otg-test.cpp - this should be sufficient
    - [ ] otg-benchmark.cpp - implement test to check for regressions and test overall performance on codesys compiler 
    - [ ] run unit tests to find more issues that sneaked in while porting
- [ ] The original code is rather functional, which TwinCAT ST doesn't benefit from a lot, rewrite to OOP where needed
- [ ] Refactor (coding conventions)
- [ ] Code cleanup and optimize performance, some parts have to be change to be faster in twincat, we do not have the power of a cpp compiler :-(
- [ ] examples
  - [ ] position.cpp
- [ ] Documentation
