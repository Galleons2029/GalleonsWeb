document.addEventListener('DOMContentLoaded', function() {
    const sendBtn = document.getElementById('send-btn');
    const userInput = document.getElementById('user-input');
    const chatHistory = document.getElementById('chat-history');

    function sendMessage() {
        const text = userInput.value.trim();

        if (text.length > 0) {
            // 显示用户输入的信息
            const userMessage = document.createElement('div');
            userMessage.className = 'user-message';
            userMessage.innerText = text;
            chatHistory.appendChild(userMessage);

            // 在此处添加与您的语言模型进行交互
            fetch('您的API接口地址', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ input: text })
            })
            .then(response => response.json())
            .then(data => {
                const modelMessage = document.createElement('div');
                modelMessage.className = 'model-message';
                modelMessage.innerText = data.output;
                chatHistory.appendChild(modelMessage);

                // 滚动至最新消息
                chatHistory.scrollTop = chatHistory.scrollHeight;
            })
            .catch(error => {
                console.error('与语言模型交互时发生错误:', error);
            });

            // 清空输入框
            userInput.value = '';
        }
    }

    // 为发送按钮添加点击事件
    sendBtn.addEventListener('click', sendMessage);

    // 为输入框添加回车事件
    userInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendMessage();
        }
    });
});

