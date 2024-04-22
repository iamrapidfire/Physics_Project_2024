import tkinter as tk
from math import *
from _wavelength_to_rgb import wavelength_to_rgb
from matplotlib.pyplot import *



# Монохроматический свет (красный) падает на плосковыпуклую линзу
# Длина волны \lambda = 700 нм
wavelength = 700 * 10**(-9) # длина волны, метров
lense_curve_radius = 1 # радиус кривизны линзы, метров


class PHYS_PROJ:
    def __init__(self) -> None:
        print("PHYS_PROJ initialized")

    def scale_change(newVal):
        PHYS_PROJ.monochromatic_newton_rings_intensivity(wavelength, lense_curve_radius)

    def newton_ring_radius(m: int, wavelength: int, lense_curve_radius: int): # функция для определения радиуса m-того светлого кольца по формуле
        return sqrt((m - 0.5) * wavelength * lense_curve_radius) # возвращает радиус в метрах
    
    def intensivity(I: int, r: int): # функция для определения интенсивности результата интерферирующих лучей, I - исходная интенсивность, r - радиус, на котором считается интенсивность
        d = lense_curve_radius - (sqrt(lense_curve_radius**2 - r**2)) # находим величину воздушного зазора в метрах в точке, находящейся в r метрах от центра
        delta = 2*d + wavelength / 2 # разность хода
        delta_phi = delta * 2 * pi / wavelength # разность фаз
        return 2 * I * (1 + cos(delta_phi)) # возвращаем результирующую интенсивность в пределах от 0 до 4 * I

    
    def monochromatic_newton_rings_intensivity(wavelength: int, lense_curve_radius: int): # функция для отрисовки интерференционной картины с использованием интенсивности
        _window_height = 500 # высота окна вывода графики
        _window_width = 500 # ширина окна вывода графики
        _center_coords = [_window_height / 2, _window_width / 2] # координаты центра окружностей

        # hor_scale = tk.Scale(orient=tk.HORIZONTAL, length=200, from_=380, to=700, variable=wavelength, command=PHYS_PROJ.scale_change)
        # hor_scale.pack()

        main_window = tk.Tk()
        main_window.geometry(f"{_window_width}x{_window_height}")
        canvas = tk.Canvas(bg="black", width=500, height=500)
        canvas.pack()

        for r in range(1, 500): # для каждого радиуса от 1 до 499 
            r /= 100000 # переводим метры 
            intens = PHYS_PROJ.intensivity(1, r)/(4 * 1) # рассчитываем интенсивность, радиус взят в миллиметрах, после этого нормируем делением на 4 * I
            color = tuple([floor(i*intens) for i in wavelength_to_rgb(wavelength * 10**9)]) # цвет - красный, интенсивность - множитель
            color = '#%02x%02x%02x' % color
            scale = 70000 # по факту, просто масштабируем
            r *= scale
            canvas.create_oval(_center_coords[0]-r, _center_coords[1]-r, \
                               _center_coords[0]+r, _center_coords[1]+r, outline=color, width=3)
        
        tk.mainloop()

    def monochromatic_newton_rings(wavelength: int, lense_curve_radius: int): # функция для отрисовки интерференционной картины без использования интенсивности
        _window_height = 500
        _window_width = 500
        _center_coords = [_window_height / 2, _window_width / 2]

        main_window = tk.Tk()
        main_window.geometry(f"{_window_width}x{_window_height}")
        canvas = tk.Canvas(bg="black", width=500, height=500)
        canvas.pack()
        for m in range(1,100):
            ring_radius = PHYS_PROJ.newton_ring_radius(m, wavelength, lense_curve_radius) # находим радиус m-того светлого кольца по формуле (в метрах)      
            ring_radius *= 100 * 1000 # переводим в миллиметры
            ring_color = '#%02x%02x%02x' % wavelength_to_rgb(wavelength * 10**9) # здесь мы можем динамически менять длину волны, и цвет картины и её характеристики будут меняться
            canvas.create_oval(_center_coords[0]-ring_radius, _center_coords[1]-ring_radius, \
                               _center_coords[0]+ring_radius, _center_coords[1]+ring_radius, outline=ring_color, width=3)
        
        tk.mainloop()



if __name__ == '__main__':
    PHYS_PROJ.monochromatic_newton_rings_intensivity(wavelength, lense_curve_radius)
    

