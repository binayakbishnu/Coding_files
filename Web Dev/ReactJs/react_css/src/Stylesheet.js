import React from 'react'
import './mystyles.css'

function Stylesheet(props) {
    let className = props.primary_class ? 'primary' : ''
    return (
        <div>
            <h1 className={className}>Stylesheets</h1>
        </div>
    )
}

export default Stylesheet
