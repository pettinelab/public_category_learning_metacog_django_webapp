// MAKES CERTAIN FORMS OR FORM FIELDS CONDITIONAL ON OTHER FORM QUESTIONS

const conditional_questions = JSON.parse(document.getElementById('conditional_questions').textContent);
// Get all the field1 inputs and add a change event listener
function changeradio(cause_question,cause_question_id,bool){
  var field1Radio = document.getElementById(cause_question_id);
  field1Radio.addEventListener("click",function() {
      for (var i = 0; i < conditional_questions[cause_question]['questions'].length; i++) {
          let conditional_question_id = `#${conditional_questions[cause_question]['questions'][i]}`;
          let field2Input = document.querySelector(conditional_question_id);
          if (field2Input.nodeName === "SELECT" || field2Input.type === "text"){
              field2Input.disabled = bool;
          }
          else{
              console.log('N Children = ' + field2Input.children.length)
              for (var ii = 0; ii < field2Input.children.length; ii++) {
                  let conditional_question_radio_id = `#${conditional_questions[cause_question]['questions'][i]}_${ii}`;
                  let field2Input_radio = document.querySelector(conditional_question_radio_id);
                  field2Input_radio.disabled = bool;
              };
          }

      };
  });
}
for (let cause_question in conditional_questions) {
  for (let i = 0; i < conditional_questions[cause_question]['enable'].length; i++) {
    let cause_question_id = `${cause_question}_${conditional_questions[cause_question]['enable'][i]}`;
    changeradio(cause_question,cause_question_id,false)
   }
  for (let i = 0; i < conditional_questions[cause_question]['disable'].length; i++) {
    let cause_question_id = `${cause_question}_${conditional_questions[cause_question]['disable'][i]}`;
    changeradio(cause_question,cause_question_id,true)
   }
}