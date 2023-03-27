# Histogram Shrinking:
    Shrinks intensity values from range [a:b] to [c:d] (where [c:d] is a subset of [a:b]).

# Histogram Stretching:
    Stretches intensity values from range [c:d] to [a:b] (where [c:d] is a subset of [a:b]).

# Notes:
   - Input image should be placed in `./image.png`
   - Depth of image is considered as 8bit (Other depths may result in an unstable output).
   - after shrinking and then stretching, the stretched image is not exactly the original image. some data is lost due to digital world charactristics.