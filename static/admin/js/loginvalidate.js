
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
    
    
     