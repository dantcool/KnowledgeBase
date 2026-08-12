SOURCES:
https://iliputer.com/how-computer-graphics-work/
https://www.tutorialspoint.com/computer_graphics/index.htm

# Definition and scope

Computer graphics can be defined as the creation, manipulation of visual images using algorithms and mathematical models. It encompasses two main categories: 2D graphics, which involve flat images displayed on a screen and 3D graphics, which create the illusion of depth and dimensional. The variety of applications relies on the complexity and capabilities of rendering techniques, hardware, and software used in creating these visuals. 

# Applications 
- Video games: 3D modeling, animation, and real-time rendering produce immersive gaming experiences
- Movies and Animation: Special effects and animated characters rely on complex rendering processes to bring stories to life 
- Simulations and Visualizations: Fields such as medicine, engineering, and geoscience utilize computer graphics to visualize data and simulations, aiding in decision-making and education 
- User interfaces: the design of web pages, applications. and operating systems relies heavily on 2D graphics to create user-friendly experiences. 

# Building Blocks of Computer Graphics 
## Hardware Components 
hardware used in computer graphics plays a critical role in performance and output quality 
Key components include:

- Graphics Processing Unit (GPU): a dedicated processor designed to accelerate the rendering of images and handle complex calculations related to graphics.Modern GPUs are essential for intensive tasks such as 3D rendering and real-time video games
- Central Processing Unit (CPU): while the GPU is optimized for parallel processing of graphics, the CPU handles the overall systems's computations, including logic, control, and processing of non-graphical tasks. 
- Memory: Graphics applications require significant memory bandwidth and capacity.Graphics cards often come equipped with dedicated video memory (VRAM) to store textures, models, and frame buffers. 

## Software Components
the software utilized in computer graphics ranges from low-level programming languages to high-level graphic design applications. Key categories include 

- Graphics APIs: Application Programming Interfaces such as OpenGL, DirectX and Vulkan provide developers with standardized methods to interface with the GPU, allowing for rendering and resource management.
- Graphic Design Software: programs like Adobe Photoshop, Blender, and Autodesk Maya are used by artists to create 2D and 3D content through a user-friendly interface. 
- Game Engines: Comprehensive systems like unity and unreal engine facilitate game development, providing built in functionality fro physics, rendering, and scripting. 


# Types of Computer Graphics
computer graphics can be broadly categorized based on their applications, nature, or the way they are generated. Here are the main types of computer graphics:

- Raster Graphics(Bitmap Graphics) - Bitmap graphics are the images made up of tiny dots called pixels(picture elements)
- Vector Graphics- images are created using mathematical equations to represent geometric shapes such as lines, circles, and polygons.
- 3D Graphics - Graphics that represent three-dimensional objects and scenes, often used for simulation, video games, and movies.
- Interactive Graphics - graphics that allow users to interact with them, typically through a user interface (UI)
- Real-Time Graphic - graphics that are rendered in real-time, meaning they are created and displayed instantly as the user interacts with them. 
# Process of Creating  Computer Graphics 

understanding how computer graphics are created involves examining several critical processes, which can be broken down into key stages. 

## 1.Modeling 

modeling is the process of creating a representation of a 3D object. This can be achieved through various techniques:

- Polygon Modeling: The most common method that uses vertices, edges, and faces to create 3D shapes. Models are often made up of thousands or millions of polygons depending on the required detail. 
- NURBS and Subdivision Surfaces: Techniques that allow for smooth curves and surfaces. NURBS (Non-uniform Rational B-Splines) provide a mathematical representation of curves, enabling the creation of smooth geometries. 

## 2.Texturing 

Texturing involves applying images (textures) to the surfaces of 3D models to give them color, detail and realism. This process typically include:

- UV Mapping: The technique of unwrapping a 3D models surface into a  2D image format to apply textures without distortion 
- Texture Types: Various textures, including diffuse maps(color), specular maps (shininess), normal maps (surface detail), and bump maps (height variations), enhance realism. 

## 3.Lighting 
lighting is crucial in setting the mood and realism of a scene. Techniques include:

- Ambient Lighting: Provides a base level of illumination uniformly in the scene 
- Directional Lighting: simulates sunlight by creating parallel light rays that cast shadows
- Point and Spot Lights: Create light sources that emit from a point in all directions (point lights) or in a specified direction (spot lights), allowing for more dynamic light interactions 

## 4. Rendering
Rendering is the final stage in creating computer graphics, transforming the 3D models, textures, and lighting into a 2D image or animation. This step can be computationally intensive, involving two principal approaches:

- Rasterization: the most common technique used in real-time applications, such as video games. It converts 3D models to pixels on a 2D screen by mapping vertices of polygon to screen coordinates. 
- Ray Tracing: a more computationally expensive method that simulates the way light interacts with objects to achieve photo realistic images. it traces the path of rays of light as they traverse the scene and interact with various surfaces. 

## 5.Animation 
Animation breathes life into models by creating the illusion of movement. this process can be divided into two main categories: 

- Key framing: Defining specific points in time where an objects position, rotation, or scale changes, and allowing the software to interpolate the intermediate frames. 
- Procedural Animation: Uses algorithms to create motion. Physics-based simulations (e.g. ragdoll effects) can be used to generate realistic movements based on environmental interactions.

## 6.Post-Processing
post-processing involves editing the rendered images or videos to enhance visual quality through effects like anti-aliasing,motion blur, and color grading. 

# Mathematics in Computer Graphics 
in Computer Graphics we make full use of mathematics including set theory, trigonometry, vector algebra, linear algebra, calculus and so on. One of the key mathematical concepts used in graphics is sets and mappings. Set helps in structuring, organizing, and transforming data efficiently. They are fundamental in various algorithms and processes in computer graphics. 
[[ Sets and Mapping ]]


