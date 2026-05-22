import { useState, useEffect } from "react";
import axios from "axios";

interface Message {
  userQuery: string;
  botResponse: string;
}

function App() {
  const [inputValue, setInputValue] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);

  async function handleSubmit() {
    if (inputValue.trim() === "") return;
    const userQuery = inputValue;
    const newMessage = {
      userQuery: userQuery,
      botResponse: "Loading...",
    };
    setMessages([...messages, newMessage]);
    setInputValue("");

    //send api request to backend
    setTimeout(async () => {
      try {
        const response = await axios.post("http://localhost:8000/api/search", {
          query: userQuery,
        });

        const botResponse = response.data.botResponse;

        setMessages((prevMessages) => {
          return [...prevMessages.slice(0, -1), { userQuery, botResponse }];
        });
      } catch (err) {
        console.error("Error calling backend", err);
        setMessages((prevMessages) => {
          return [
            ...prevMessages.slice(0, -1),
            { userQuery, botResponse: "Server error" },
          ];
        });
      }
    }, 2000);
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

  useEffect(() => {
    const checkBackend = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/health");
        console.log(response.data);
      } catch (err) {
        console.error("Backend error: ", err);
      }
    };

    checkBackend();
  }, []);

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
