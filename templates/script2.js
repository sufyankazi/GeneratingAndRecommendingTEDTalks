    const quizContainer = document.getElementById("quiz");

    const submitButton = document.getElementById("submit");
    function showResults() {
        const userinput = document.getElementById("userinput").value;
        // gather answer containers from our quiz
	$.ajax({
         type: "POST",
         contentType: "application/json; charset=utf-8",
         url: "/booyah",
         dataType: "json",
         async: true,
         data: "{"+userinput+"}",
         success: function (data) {
           resultsContainer.innerHTML = `${data}`;},
 	 error: function (result) {
		 resultsContainer.innerHTML = `Big Error`;}
         
       })

    // on submit, show results
    submitButton.addEventListener("click", showResults);
};
