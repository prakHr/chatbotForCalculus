from sympy import sympify
from sympy import Poly,Symbol,summation,pprint,solve,Integral,Derivative
from sympy import solve_poly_inequality,solve_rational_inequalities,solve_univariate_inequality,sin
import pyAlgebra
from pyAlgebra import *    
     
from arielai import Chatbot, ChatUI
from arielai.backends import BaseBackend
# import traceback

def launch_chatbot():
    class MyBackend(BaseBackend):
        def generate(self, St, history, **kwargs):
            try:
                SI=find_indefinite_integral(St,'x')      
                SD=find_derivative(St,'x')  
                return f"Here is the indefinite integral: {SI} \n and here is the derivative: {SD}"
            except Exception as e:
                return f"Sorry, I couldn't process your input. Please make sure to input a valid function of x. Error: {str(e)}"
    bot = Chatbot(
        backend_instance=MyBackend()
    )
    ui = ChatUI(
        bot,
        brand_name="Integral And Differentiation Calculus Calculator Bot, Please input a function of x to find its indefinite integral and derivative",
        accent="indigo",        # color theme
        dark_mode=False,        # or True for dark
        show_footer= True,
        footer_link="https://github.com/prakHr/pyAlgebra-v/blob/main/Demo_pyAlgebra.ipynb",
        footer_text="Built with ArielAI"
    )
    ui.launch(share=False)

if __name__ == "__main__":
    launch_chatbot()