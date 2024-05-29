from django.shortcuts import render

# Create your views here.

def calculate(request):
  if request.method == 'POST':
    first_number = float(request.POST['first_number'])
    second_number = float(request.POST['second_number'])
    operation = request.POST['operation']

    if operation == '+':
      result = first_number + second_number
    elif operation == '-':
      result = first_number - second_number
    elif operation == '*':
      result = first_number * second_number
    elif operation == '/':
      if second_number == 0:
        result = "Division by zero is not allowed!"
      else:
        result = first_number / second_number
    else:
      result = "Invalid operation!"
  else:
    result = ""
  return render(request, 'calc/calculator.html', {'result': result})
