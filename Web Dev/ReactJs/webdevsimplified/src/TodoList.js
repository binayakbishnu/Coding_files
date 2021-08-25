import React from 'react'
import Todo from './Todo'

export default function TodoList({ todos }) {
    return (
        // <div>
        //     {/* Hello World */}
        //     {todos.length}
        // </div>
        todos.map(todo=>{
            return <Todo todo={todo}/>
        })
    )
}
