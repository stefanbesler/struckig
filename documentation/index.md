# Struckig

<div align="center">
  <h3 align="center">
    Online Trajectory Generation. Real-time. Time-optimal. Jerk-constrained.<br/>
    "Full" port from C++ to Structured Text, TwinCAT 3.
  </h3>
</div>

This library is a port of [pantor/ruckig](https://github.com/pantor/ruckig) to **IEC61131-3 Structured Text** and brings free software powered Online Trajectory Generation to Codesys and TwinCAT 3. The library is dual licenced. You can use it under the terms of [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html), which summarized says that you can use it, redistribute it, study it, modify it as long as you distribute your code **under the same terms and conditions**. If you do not agree with the terms of the GPL and want to keep your source closed, [contact me](mailto:stefan@besler.me) to get a commercial license for struckig.

## Why GPLv3

While a lot of free software projects nowadays use the **MIT license** instead of the **GPLv3 license**, I decided to use the latter one for *struckig*. Free software, or as people like to call it open-source software, is not the same as **free beer**. You should either value its principles by using a copy-left license on your source code as well, or if you can not you should contribute to the community, which is using their **spare time** to implement this kind of software. For this project you can do this by supporting [pantor by getting a pro version of ruckig](https://ruckig.com/) or by [contacting me for support with struckig](mailto:stefan@besler.me).

## Install Struckig

Before you can use this library to blazingly fast calculate trajectories for your PLC project, you'll need to install it. You can either compile the library ourself or, easier, use a precompiled library. *Struckig* doesn't have any dependencies to properitary libraries, so usually the precompiled library *just works*.

<button onClick="location.href='userguide/installation.html'" type="button">Install.</button>

## Getting started

After you installed struckig you are ready to use it, but still have to reference it in your PLC, learn how to add the *struckig* library to your PLC and how to use it to calculate your very first trajectory.

<button onClick="location.href='userguide/installation.html'" type="button">Try.</button>

## Documentation

The API reference provides insights into the internals of struckig.

<button onClick="location.href='reference/Struckig/Constants.html'" type="button">Read the docs.</button>
