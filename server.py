from flask import Flask, render_template, request, redirect, session, flash
from entries import InfoForm, QuizForm
from database import insert_records, get_record_by_fullname, update_score

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kodlandprojectkey'


@app.route('/info', methods=['GET', 'POST'])
def info():
    info_form = InfoForm()

    if request.method == 'POST':
        fullname = info_form.fullname.data
        color = info_form.color.data
        animal = info_form.animal.data
        hobbies = info_form.hobbies.data
        score = 0

        try:
            # Save to database
            insert_records(fullname, color, animal, hobbies, score)

            # Verify entry creation
            if get_record_by_fullname(fullname) is not None:
                session['fullname'] = fullname
                flash("User information saved successfully!", "success")
                return redirect('/quiz')
            else:
                flash("Failed to save user information.", "error")
        except Exception as e:
            flash(f"An error occurred: {e}", "error")
            print(f"Error: {e}")

    return render_template('info.html', form=info_form)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    quiz_form = QuizForm()
    score = session.get('score', 0)
    best_score = session.get('best_score', 0)

    # Retrieve fullname from session
    fullname = session.get('fullname')

    if request.method == 'POST':
        # Retrieve the best score from the session or database
        current_record = get_record_by_fullname(fullname)
        if current_record:
            best_score = current_record[4]

        score = calculate_score(quiz_form)
        session['score'] = score

        # Retrieve the current score for the user
        current_record = get_record_by_fullname(fullname)
        if current_record:
            if score > current_record[4]:
                update_score(fullname, score)
                best_score = score
                session['best_score'] = best_score

        return redirect('/quiz')

    return render_template('quiz.html', form=quiz_form, score=score, best_score=best_score)


def calculate_score(form):
    correct_answers = {
        'q1': '3',
        'q2': '2',
        'q3': '1',
        'q4': '1',
        'q5': '1'
    }

    score = 0

    for question, correct_answer in correct_answers.items():
        if getattr(form, question).data == correct_answer:
            score += 20

    return score


if __name__ == '__main__':
    app.run(debug=True)
