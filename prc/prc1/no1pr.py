import numpy as np 
 # وارد کردن کتابخانه numpy با نام np
import matplotlib.pyplot as plt 
 # وارد کردن کتابخانه matplotlib.pyplot با نام plt

x = np.linspace(0, 2*np.pi, 100) 
 # تولید یک آرایه از اعداد بین 0 تا 2*pi با 100 نمونه

y_sin = np.sin(x) 
 # محاسبه مقادیر سینوس برای هر نقطه در x
y_cos = np.cos(x)  
# محاسبه مقادیر کسینوس برای هر نقطه در x

plt.plot(x, y_sin, label='Sine')  
# رسم نمودار سینوس با برچسب "Sine"
plt.plot(x, y_cos, label='Cosine') 
 # رسم نمودار کسینوس با برچسب "Cosine"

plt.fill_between(x, y_sin, y_cos, color='gray', alpha=0.3) 
 # پر کردن فضا بین نمودارهای سینوس و کسینوس با رنگ خاکستری و شفافیت 0.3

plt.xlabel('Angle (radians)')  
# تعیین برچسب محور x به "Angle (radians)"
plt.ylabel('Value') 
 # تعیین برچسب محور y به "Value"
plt.title('Sine and Cosine Plot with Hatched Shading') 
 # تعیین عنوان نمودار به "Sine and Cosine Plot with Hatched Shading"
plt.legend()  
# نمایش لیست توضیحات

plt.show() 
 # نمایش نمودار