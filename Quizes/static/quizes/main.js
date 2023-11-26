
const url = window.location.href

const quizes = [...document.getElementsByClassName('quizes')]

function StartQuiz() {
    quizes.forEach(quiz=> quiz.addEventListener('click',()=>{
        const id = quiz.getAttribute('id')
        window.location.href = url + id
    }))
}

function QuizSwipper(){
    console.log(id)
}