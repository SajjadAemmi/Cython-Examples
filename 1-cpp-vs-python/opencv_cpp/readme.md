# C++ Convolution

Compile it using a C++ compiler, e.g., g++.

```bash
g++ -std=c++11 convolution.cpp -o convolution \
    -I/opt/homebrew/Cellar/opencv/4.10.0_18/include/opencv4 \
    -L/opt/homebrew/Cellar/opencv/4.10.0_18/lib \
    -lopencv_core -lopencv_imgcodecs -lopencv_highgui
```

Run the compiled program:

```bash
./convolution
```
