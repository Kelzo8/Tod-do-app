import streamlit as st
import functions #backend

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My To-do APP")
st.subheader("This is my To-do APP")
st.write("This app is to increase your productivity.")

#enumerate keeps track of loops
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a Todo....",
              on_change=add_todo, key='new_todo')

