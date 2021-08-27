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

  const LOCAL_STORAGE_KEY = 'todoApp.todos'

  useEffect(() => {
    //? to load stored todos
    const storedTodos = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY))
    //?parsing to make it string obj
    if (storedTodos)
      setTodos(storedTodos)
    //^ if statement to prevent loading if empty
  }, [])  //? ,empty therefore function called once
  //^ id when storing locally
  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(todos))
  },
    //? the below array list dependencies which if changed will call the function
    [todos])
  //^ only stores but does not load

  function handleAddTodo() {
    const name = todoNameRef.current.value
    if (name === '') return
    // console.log(name)
    setTodos(prevTodos => {
      // to access prev todos to clear all of them
      // return [...prevTodos,{id:1,name:name,complete:false}]
      //^ but the id remains same (ie, 1) therefore download library to generate random ones : uuid library
      return [...prevTodos, { id: uuid(), name: name, complete: false }]
      //! but todos erased when reloaded: use useEffect to store locally
    })
    todoNameRef.current.value = null  //to clear input after clicking add button
  }

  function toggleTodo(id){
    //? toggle on/off todos
    const newTodos = [...todos]
    //? ^copy made to not change original state varaible
    //! always do this
    const todo = newTodos.find(todo =>todo.id === id)
    todo.complete = !todo.complete
    setTodos(newTodos)
  }

  function handleClearTodo(){
    const newTodos = todos.filter(todo =>!todo.complete)
    setTodos(newTodos)
  }

  return (
    <>
      {/* <TodoList todos={todos} /> */}
      {/* after adding toggleTodo... */}
      <TodoList todos={todos} toggleTodo={toggleTodo}/>
      <input ref={todoNameRef} type="text"></input>
      <button onClick={handleAddTodo}>Add Todo</button>
      <button onClick={handleClearTodo}>Clear Completed</button>
      {/* <div>0 left to do</div> */}
      <div>{todos.filter(todo=>!todo.complete).length} left to do</div>
    </>
  );
}

export default App;
