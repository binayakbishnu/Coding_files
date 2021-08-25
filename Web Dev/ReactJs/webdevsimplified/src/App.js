import React, { useState, useRef, useEffect } from 'react';
//! ^^{ useState } to define state
//! ^^ { useRef } to enable referencing elements, here, to be able to take input
//! to store todos in locally to prevent deletion in reloads

import TodoList from "./TodoList";

import { v4 as uuid } from "uuid";

function App() {
  // const [todos,setTodos] = useState(['Todo 1','Todo 2'])
  //? first member is all of the todos
  //? and setTodos is the function to create/change each

  // const [todos, setTodos] = useState([{ id: 1, name: 'todo1', complete: false }])
  const [todos, setTodos] = useState([])

  const todoNameRef = useRef()

  function handleAddTodo(e) {
    const name = todoNameRef.current.value
    if (name === '') return
    // console.log(name)
    setTodos(prevTodos => {
      // to access prev todos to clear all of them
      // return [...prevTodos,{id:1,name:name,complete:false}]
      //^ but the id remains same (ie, 1) therefore download library to generate random ones : uuid library
      return [...prevTodos, { id: uuid(), name: name, complete: false }]
      //! but todos erased when reloaded: use useEffect to stroe locally
    })
    todoNameRef.current.value = null  //to clear input after clicking add button
  }

  const LOCAL_STORAGE_KEY = 'todoApp.todos'
  //^ id when storing locally
  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(todos))
  },
    //? the below array list dependencies which if changed will call the function
    [todos])
  //^ only stores but does not load, therefore use...
  useEffect(() => {
    const storedTodos = localStorage.getItem(LOCAL_STORAGE_KEY)
    if (storedTodos) setTodos(storedTodos)
    //^ if statement to prevent loading if empty
  }, [])  //? ,empty therefore function called once


  return (
    <>
      <TodoList todos={todos} />
      <input ref={todoNameRef} type="text"></input>
      <button onClick={handleAddTodo}>Add Todo</button>
      <button>Clear Completed</button>
      <div>0 left to do</div>
    </>
  );
}

export default App;
