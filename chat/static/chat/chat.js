const userName = JSON.parse(document.getElementById('json-username').textContent);
const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
let date = new Date();
const roomDate = date.toLocaleString();
            
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + roomName
    + '/'
);

let messages = document.querySelector('.message-area');

document.querySelector('#down').onclick = function(e) {
    messages.scrollTo({
        top: 20000,
        behavior: "smooth"
    })
}
            
document.querySelector('#up').onclick = function(e) {
    messages.scrollTo({
        top: 0,
        behavior: "smooth"
    })
}

chatSocket.onmessage = function(e) {
    console.log('на связи');
    console.log(roomDate);


    const data = JSON.parse(e.data);

    if(data.message){
        let html;
        if(data.username == userName){
            html = '<div class="p-4 bg-gray-200 rounded-xl text-end">';
            } else {
                html = '<div class="p-4 bg-gray-200 rounded-xl text-start">';
            }
            html += '<p class="fs-3 fst-italic">' + data.username + '</p>';
            html += '<p class="badge bg-secondary text-wrap fs-5">' + data.message + '</p>';
            html += '<p>' + data.date + '</p></div>';
        document.querySelector('.message-area').innerHTML += html;
                    
        messages.scrollTo({
            top: 20000,
            behavior: "smooth"
        })                    
    }
}

chatSocket.onclose = function (e) {
    console.log('обрыв связи');
}

document.querySelector('#go').onclick = function(e) {
    const messageInputDom = document.querySelector('#msg');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName,
        'date': roomDate,
    }));

    messageInputDom.value = '';
}

document.onkeydown=key;
function key(){
    window.status=event.keyCode;
    if(event.keyCode==13){
        document.getElementById("go").click();
    }
}