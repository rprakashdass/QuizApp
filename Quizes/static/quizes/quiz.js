const url = window.location.href
const answerBox = document.getElementById('answer-box')

$.ajax({
    type:'GET',
    url:`${url}question`,
    success:function(response){
       const questions = response.question
        questions.forEach(element => {
            for(const[question, answers] of Object.entries(element)){
                answerBox.innerHTML +=`<hr>
                <div>
                <p>${question}</p>
                </div>
                `
                answers.forEach(answer=>{
                    answerBox.innerHTML += `
                    <div>
                    <input type="radio" class="answer" id="${question}-${answer}" name="${question}" value="${answer}">
                    <label for=${question}>${answer}<label>
                    </div>
                    `
                })
            }
        });
    },
    error:function(error){
        console.log(error)
    }
})

const AnswerSpace = document.getElementById('answer-space')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const answer = [...document.getElementsByClassName('answer')]

const validate = () => {
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    answer.forEach(ans=>{
        if(ans.checked){
            data[ans.name] = ans.value
        } else{
            if(!data[ans.name]){
                data[ans.name] = null
            }
        }
    })

    $.ajax({
        type:'POST',
        url:`${url}submit/`,
        data:data,
        success : function(response){
            console.log(response)
        },
        error:function(error){
            console.log(error)
        }
    })
}

AnswerSpace.addEventListener('submit', ans=>{
    ans.preventDefault()
    validate()
})