import React from 'react'

// export default function Todo({ todo }) {
//* adding toggleTodo
export default function Todo({ todo, toggleTodo }) {
    function handleTodoChange() {
        //? seperate function made so that id can be passed
        toggleTodo(todo.id)
    }
    return (
        <div>
            {/* {todo} */}

            {/* after making id name attrs */}
            {/* {todo.name} */}
            {/* making checkboxes to show completion */}
            <label>
                {/* <input type="checkbox" checked={todo.complete}></input> */}
                <input type="checkbox" checked={todo.complete} onChange={handleTodoChange}></input>
                {todo.name}
            </label>
        </div>
    )
}
