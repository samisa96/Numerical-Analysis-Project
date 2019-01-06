![alt text](https://i.imgur.com/ZNpFSo2.png)

# User-Guide : Numerical-Analysis-Project

This project will allow the user to approximate roots of functions using several methods
and to approximate results of matrix.
Some of the "roots approxmiates methods" will be backup with graphs.

#### Roots approximation methods:
1. The Bisection method.
2. Newton raphson method
3. Secant method.

#### Interpolation methods:
1. Poly approximation
2. Linear approximation
3. La-Grange
4. Neville
5. Cubic Spline

#### Matrix approximation methods:
1. Gauss Siedle
2. Jacobi
3. SOR - Successive Over Relaxation

#### Integration Quadratures:
1. Romberg
2. Simpson
3. Trapezoid
4. Gaussian Quadrature

## Getting Started
#### Prerequisites

A work environment that supports Python3, like Pycharm, VS code etc.
_____________________

A quick introduction of the minimal setup you need to get a "Numerical-Analysis-Project" up & running.
Open folder for this project and clone this repository.
Use the following command:
```
git@github.com:yariv1025/Numerical-Analysis-Project.git
```
After Python installion, open cmd / Terminal, navigate to project folder and run the following command:
```
python pip install -r install.txt
```

Project Structure
------------------
The tree below displays the files and folders structure:
```
├── Docs                            # Documents of project:
|  |── Diagrams                     # Contain all relevant DFD's
|  ├── Summery                      # Short summery of the methods
|  └── Final summery                # Hackathon - final summery  
├── Lib                             # All methods files - Python
|   ├── Bisection_method.py
|   ├── CubicSpline_method.py
|   ├── GaussSiedle_method.py
|   ├── GaussSiedle_SOR.py          # Unused!
|   ├── Hackathon.py                # Unused!
|   ├── Jacobi_method.py
|   ├── Lagrange                    # Unused!
|   ├── LaGrange_method.py 
|   ├── Linear aprox.py
|   ├── Main.py
|   ├── MatrixInversion_method.py
|   ├── Neville_method.py
|   ├── NewtonRephson_method
|   ├── plot_it.py
|   ├── Poly_aprox.py   
|   ├── Romberg_method.py
|   ├── Secant_method.py
|   ├── Simpson_method.py
|   ├── SOR_method.py
|   ├── Trapezoid_method.py
|   └── Gaussian Quadrature.py
├── readme.md                       # User guide
├── install.txt                     # text file for installation
└── .gitignore                      # Files we ignored

```
*Some methods include ready-to-run examples.

Built With
----------
* [Pycharm](https://www.jetbrains.com/pycharm/) -Python IDE.
* [Scipy, Sympy, Numpy, Matplotlib](https://www.scipy.org/) -Python-based ecosystem software for mathematics, science, and engineering.

Authors
-------
Students in the software engineering department at SCE - Sami Shamoon College:
* [Alon Gabay](https://github.com/alongabay)
* [Yariv Garala](https://github.com/yariv1025)
* [Almog Machlof](https://github.com/Almogma)
* [Elad Metudi]()
* [Tom Zeiger](https://github.com/TomZaiger)
* [Shirel Biton](https://github.com/shirelBiton)
* [Liz Ohayon](https://github.com/lizohayon)
* [Yakir Kobaivanov](https://github.com/yakirk1)

See also the list of [contributors](https://github.com/yariv1025/Numerical_Analysis_Project/graphs/contributors) who participated in this project

License
-------
This project is licensed under the SCE License - see the [License.md](https://gist.github.com/Numerical_Analysis_Project/LICENSE.md) file for  details.

Acknowledgments
---------------
* [matplotlib](https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html) - We used matplotlib code to export a graph for given function.
## END
