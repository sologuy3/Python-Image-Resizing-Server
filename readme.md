#Image Resizing Server in Python

#####Note: Project is still a work in progress

A basic image resizing server written in Python.
Images in the img_src folder can be requested in original format, or 

* transformed into a custom size 
* reduced/increased by a scale factor or 
* transformed such that either the width or height is fits a requested value.

Ideal for use with a CDN such as AWS Cloudfront. A request from a client to the CDN will trigger a request to this server with a matching filename. 

Since the filename contains the size/scale details of the image, this service will respond with the correctly transformed image, which will then be cached by the CDN.

### URL Syntax
#### Original Image 
`/original@<image_name>`
#### Custom Dimensions
`/resize@widthxheight:<image_name>`
Example: `/resize@200x200:canihaz.jpg`

#### Size to Scale
`/resize@4:<image_name>`

#### Fit Dimension maintaining Ratio
`/fit@widthx0:<image_name>`
or
`/fit@0xheight:<image_name>`

### Example

Client makes the following request to the CDN: 
`GET cdnurl.com/resize@100x500:canihaz.jpg HTTP/1.1`

CDN does not have that image on file, so requests the image from the server - `GET imgserver.com:port/resize@100x500:canihaz.jpg HTTP/1.1`

Server confirms that the original image is not in that size, performs the image transform and responds to the CDN.

CDN then caches the image in that size under resize@100x500:canihaz.jpg and is able to respond to clients immediately using the cached version of this image. 


