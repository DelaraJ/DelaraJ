---
layout: posts
title: The general process of the Mandelbrot project
---


<img src="/assets/images/sophia-interview.gif"
    alt="sophia-interview"
    style="float; margin-right: 10px;"  />


*The brief of the project we wanted to do was to produce an audio-visual artwork using programming. The most interesting point of this, is that we can think of an image or music and implement it.*

To do this project, I followed these steps:
1. Using Python language for ideation and initial implementation
2. Using C language to produce final images
3. Using Sonic Pi to produce music
4. Using ffmpeg to convert images and music to video

-We use Python to start the project because Python has libraries that remove the initial complexity and allow us to focus on image selection (selecting the desired fractal and color).

The first production images:
<img src="/assets/images/firstmandelbrot.jpg"
    alt="firstmandelbrot"
    style="float; margin-right: 10px;"  />

<img src="/assets/images/juliaset.jpg"
    alt="juliaset"
    style="float; margin-right: 10px;"  />

Final image:
<img src="/assets/images/1final.jpg"
    alt="1final"
    style="float; margin-right: 10px;"  />

-Once we've chosen the desired image and figured out what we want to do in general, we move on to the C language implementation (at the end we use C because it is much faster than Python).
First, we generate the initial image and then we will implement the functions that we want to use for video production and finally, we choose the desired color and choose a path to navigate on our fractal that is visually more beautiful.
My initial image in c with simple coloring:

<img src="/assets/images/firstcimage.jpg"
    alt="firstcimage"
    style="float; margin-right: 10px;"  />

For coloring, in python we used hsv but in c we can only use rgb, so we need to use a function to convert hsv to rgb
here is some coloring that I test them:
<img src="/assets/images/00000.jpg"
    alt="00000"
    style="float; margin-right: 10px;"  />
<img src="/assets/images/00001.jpg"
    alt="00001"
    style="float; margin-right: 10px;"  />
<img src="/assets/images/00002.jpg"
    alt="00002"
    style="float; margin-right: 10px;"  />
<img src="/assets/images/00003.jpg"
    alt="00003"
    style="float; margin-right: 10px;"  />

and here is the final color that I chose:
<img src="/assets/images/00004.jpg"
    alt="00004"
    style="float; margin-right: 10px;"  />

-To complete this work of art, we need to produce the appropriate music; We use Sonic Pi to produce music with programming. Producing music with it is not difficult, the hard part is producing music in harmony with the images, both in terms of coordination with the movements and in terms of matching the initial sense of the image (with respect to color) and the beginning of the music and its rhythm. Of course, how to continue the music so as not to make the video boring is also one of the important issues.

-After all these steps, we produce the final video using ffmpeg.

---
**Test**: This is atest