from flask import Flask, jsonify, request
from langchain_utils.llm_chain import movie_chain


app = Flask(__name__)
    
    
@app.route('/ask_movie', methods=['POST'])
def ask_movie():
    try:
        data = request.json
        response = movie_chain.invoke(data)
        movies = []
        for movie in response.__dict__['movies']:
            movies.append(movie.__dict__)
            print(f"movie = {movie.__dict__}")
        return jsonify({'movies': movies})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/employee', methods=['GET'])
def employee_data():
    try:
        return jsonify({'name': "Tussar","salary":400000})
    except Exception as e:
        return jsonify({"error": str(e)})
    
    
if __name__ == '__main__':
    app.run(debug=True)

def predict_future_expenses(restaurant_id):
    # Fetch the restaurant details
    restaurant = Restaurant.objects.get(id=restaurant_id)
    
    # Fetch the existing food and electricity expenses
    food_expenses = FoodExpense.objects.filter(restaurant=restaurant).order_by('date')
    electricity_expenses = ElectricityExpense.objects.filter(restaurant=restaurant).order_by('date')

    # Format the expenses data as a prompt
    prompt = f"Restaurant: {restaurant.name}\nLocation: {restaurant.location}\nCuisine Type: {restaurant.cuisine_type}\n"
    prompt += f"Seating Capacity: {restaurant.seating_capacity}\nRating: {restaurant.rating}\nOpened Year: {restaurant.opened_year}\n\n"
    
    prompt += "Food Expenses:\n"
    for expense in food_expenses:
        prompt += f"Date: {expense.date}, Amount: {expense.amount}, Description: {expense.description}\n"
    
    prompt += "\nElectricity Expenses:\n"
    for expense in electricity_expenses:
        prompt += f"Date: {expense.date}, Amount: {expense.amount}, Description: {expense.description}\n"

    prompt += "\nGiven the above data, predict the next month's food and electricity expenses for this restaurant."

    # Use OpenAI's API to get a prediction
    print(f"prompt is :- {prompt}")
    openai.api_key = OPEN_AI_KEY
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50,
        stop=["\n"]
    )

    # Return the prediction
    print(f"response is :- {response}")
    return response.choices[0].text.strip()