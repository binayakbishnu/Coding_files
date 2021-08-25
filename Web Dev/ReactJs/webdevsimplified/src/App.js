import React, { useState } from 'react';
//! ^^{ useState } to define state

import TodoList from "./TodoList";

function App() {
  const [todos,setTodos] = useState(['Todo 1','Todo 2'])
  //? first member is all of the todos
  //? and setTodos is the function to create/change each
  return (
    <>
    <TodoList todos={todos} />
    <input type="text"></input>
    <button>Add Todo</button>
    <button>Clear Completed</button>
    <div>0 left to do</div>
    </>
  );
}

export default App;
