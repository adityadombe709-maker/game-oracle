import { useState } from "react";

interface Message {
  userQuery: string;
  botResponse: string;
}

function App() {
  const [inputValue, setInputValue] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);

  function handleSubmit() {
    if (inputValue.trim() === "") return;
    const newMessage = {
      userQuery: inputValue,
      botResponse: `Bot: Your query: ${inputValue}`,
    };

    setMessages([...messages, newMessage]);
    setInputValue("");
  }

  function displayMessages() {
    return messages.map((msg, index) => {
      return (
        <div key={index}>
          <p>You: {msg.userQuery}</p>
          <p>{msg.botResponse}</p>
        </div>
      );
    });
  }

  return (
    <>
      <input
        type="text"
        placeholder="Enter your query here"
        name="inputQuery"
        value={inputValue}
        onChange={(e) => {
          setInputValue(e.target.value);
        }}
      />
      <button onClick={handleSubmit}>Submit</button>

      {displayMessages()}
    </>
  );
}

export default App;
