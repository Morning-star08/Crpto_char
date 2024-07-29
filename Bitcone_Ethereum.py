import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("default")
datas = pd.read_excel("crpto_cu.xlsx")
plt.plot(datas["Year"], datas["bit"], color= "black", linestyle= "dashdot",  marker= "D",markerfacecolor="blue", label= "Bitcone")
plt.plot(datas["Year"], datas["Etherenum"], color= "red", linestyle= "solid", marker= "o",markerfacecolor="black", label= "Etherenum")
plt.plot(datas["Year"], datas["Tether USDt"], color= "red", linestyle= "dashed", marker= "^", label= "Tether USD")
plt.plot(datas["Year"], datas["BNB"], color= "blue", linestyle= "dashdot", marker= "*", label= "BNB")
plt.legend()
plt.title("Rate Of Crypto", font="Poppins", fontweight="bold", fontsize="12")
plt.ylabel("Crypto Currency", fontweight= "bold",font="Poppins")
plt.xlabel("Year", fontweight="bold",font="Poppins")
plt.grid()
plt.show()
