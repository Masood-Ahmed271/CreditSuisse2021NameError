import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluateAsteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result =[]
    a_dict ={}
    for test_case in data['test_cases']:
        answer = asteroid(test_case)
        a_dict["input"] = test_case
        a_dict['score'] = answer[0]
        a_dict['origin'] = answer[1]
        result.append(a_dict)

    # result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    # return json.dumps(result)
    return jsonify(result)


def asteroid(astroidLine):
    # checking if the given asteroid line is palindrome

    answer = []
    isPalindrome = False
    score = 0
    total = 0
    character = 'A'
    if astroidLine == astroidLine[::-1]:
        isPalindrome = True

    middle = int(len(astroidLine)/2)
    origin = middle
    if isPalindrome == True:
        score+= 1
        character = astroidLine[middle]
    
    for i in range(middle-1, -1, -1):
        if astroidLine[i] == character:
            score+= 1
        else:
            if score < 7:
                total = total + score*2
            elif score >= 7 and score < 10:
                total = total + score*2*1.5
            else:
                total = total + score*2*2
            
            score = 1
            character = astroidLine[i]
        if i == 0:
            if score < 7:
                total = total + score*2
            elif score >= 7 and score < 10:
                total = total + score*2*1.5
            else:
                total = total + score*2*2
    
    if len(astroidLine)%2 != 0:
        total -= 1

    answer.append(total)
    answer.append(origin)

    return answer

    








