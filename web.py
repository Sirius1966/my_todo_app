import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():

    # st.session_state[] contains the events of the widgets as a dictionary
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# to run the web app terminal streamlit run web.py
# the order of the methods in the program
# gives the order of the appearance in the web app
# every time you refresh[⌘ + R or ↪️] the webpage the program will be executed

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # it deletes the to_do item of the session_state dictionary
        del st.session_state[todo]
        # experimental_rerun() refreshes the wep app
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")

