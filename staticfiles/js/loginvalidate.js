
    function validateForm() {
        var user = document.forms['user']["email"].value;
        var password = document.forms['user']['password'].value;
    
        if ( user == null || user == "") {
            alert("아이디를 입력해주세요.");
            return false;
        }
        if ( password == null || password == "") {
            alert("비밀번호를 입력해주세요.");
            return false;
        }
    }

    function validateForm_signup() {
        var user = document.forms['user']["email"].value;
        var password1 = document.forms['user']['password1'].value;
        var password2 = document.forms['user']['password2'].value;


    
        if ( user == null || user == "") {
            alert("아이디를 입력해주세요.");
            return false;
        }

        if(user.length<3)
        {
            alert("아이디는 3글자 이상으로 입력해주세요.");
            return false;
        }


        if ( password1 == null || password1 == "") {
            alert("비밀번호를 입력해주세요.");
            return false;
        }
        if ( password2 == null || password2 == "") {
            alert("비밀번호 확인란를 입력해주세요.");
            return false;
        }
    }
    
    
     