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

# Porting progress

- [x] Crude initial port of source code
- [x] Check source code for obvious copy & paste errors that may have occured during the port
- [x] Manual testing
- [x] Initial commit
- [x] Implement unit tests with TcUnit-Runner or use TcUnit-Wrapper to put aside this dependency
    - [ ] otg-test.cpp - this should be sufficient
    - [ ] otg-benchmark.cpp - implement test to check for regressions and test overall performance on codesys compiler 
    - [ ] run unit tests to find more issues that sneaked in while porting
- [ ] The original code is rather functional, which TwinCAT ST doesn't benefit from a lot, rewrite to OOP where needed
- [ ] Refactor (coding conventions)
- [ ] Code cleanup and optimize performance, some parts have to be change to be faster in twincat, we do not have the power of a cpp compiler :-(
- [x] examples
  - [x] position.cpp
- [ ] Documentation

# Example

The following (advanced) examples shows how to use (st)ruckig to calculate a 2-step positioning profile for a single axis.
 - The first step moves the axis from a start position (47mm) to a target position (18mm) with a *high* velocity and an end-velocity of -50mm/s.
 - From that point the profile is *switched* such that the axis continues to moves "slowly" (speed: 50mm/s) to its final destination (9mm) 
   where the axis stops    moving.
```

PROGRAM Example02_PositionProfile_2Steps
VAR
  ruckig : Ruckig(0.001);
  input_step1 : InputParameter(1) := (synchronizationType := SynchronizationTypeEnum.none,
                                      max_velocity :=         [ 1200.0 ],
                                      max_acceleration :=     [ 25000.0 ],
                                      max_jerk :=             [ 25000.0 / 0.008 ], // ~ s-time = 8ms
                                      current_position :=     [ 47.0 ],
                                      current_velocity :=     [ 0.0 ],
                                      current_acceleration := [ 0.0 ],
                                      target_position :=      [ 18.0 ],
                                      target_velocity :=      [ -50.0 ],
                                      target_acceleration :=  [ 0.0 ]);
  input_step2 : InputParameter(1) := (max_velocity :=         [ 50.0 ], // limit velocity to end-velocity of first step
                                      target_position :=      [ 9.0 ],
                                      target_velocity :=      [ 0.0 ],
                                      target_acceleration :=  [ 0.0 ]);
  input : REFERENCE TO InputParameter REF= input_step1;                                    
  output : OutputParameter;    
  run : BOOL;
  switched : BOOL;
END_VAR

// =====================================================================================================================

IF run
THEN
  ruckig.update(input, output);
  
  // switch to second profile
  IF NOT ruckig.isBusy() AND_THEN NOT switched
  THEN
    switched := TRUE;
    input.max_velocity := input_step2.max_velocity;    
    input.target_position := input_step2.target_position;
    input.target_velocity := input_step2.target_velocity;    
    input.target_acceleration := input_step2.target_acceleration;
  END_IF
  
  input.current_position := output.new_position;
  input.current_velocity := output.new_velocity;
  input.current_acceleration := output.new_acceleration;
END_IF
```

![image](https://user-images.githubusercontent.com/11271989/126785368-205a491b-0acb-4a52-8b90-a6e3f1283a18.png)

