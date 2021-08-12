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
