import random
import gradio as gr

#generates random list
def generate_list():
    arr = (random.sample(range(1,50),10))
    display = f"Random List:\n{arr}"
    return display, arr

#runs the search
def linear_search_on_state(user_number, arr_state):
    if not arr_state:
        list_msg = "Click 'Generate List' first"
        return list_msg, "⚠️ Click 'Generate List' first" # Return to update result box too

    try:
        target = int(user_number)
    except (TypeError, ValueError):
        return (
            f"⚠️ Enter a valid integer.",
            "⚠️ Enter a valid integer."
        )

    arr = arr_state[:]  #makes a copy for safety
    
    #Linear Search Logic
    found = False
    index = -1
    
    #stores the text representation of each comparison
    steps = [] 
    
    for i, val in enumerate(arr):
        steps.append(f"Iteration {i}: Comparing {target} with {val}. Is it a match? {'✅Yes' if val == target else '❌No'}")
        if val == target:
            found = True
            index = i
            break
            
    #produces final message and steps summary 
    if found:
        final_msg = f"✅ {target} found at index {index}"
    else:
        final_msg = f"❌ {target} not in generated list"
        
    steps_summary = "\n".join(steps)
    
    return final_msg, steps_summary

with gr.Blocks(title="Linear Search Game") as demo:
    gr.Markdown(
        """
        # 🎯 Linear Search Game — Two-Stage
        **Step 1:** Click **Generate List** (10 unique numbers in 1–49).  
        **Step 2:** Enter a number and click **Run Linear Search**.
        **This will show how the program goes through list and compares the target value with the values on the list.**
        """
    )
    arr_state = gr.State([])
    
    with gr.Row():
        gen_btn = gr.Button("Generate List 🎲", variant="secondary")
        user_number = gr.Number(label="Enter a number to search (1–49)", value=1, precision=0)
        run_btn = gr.Button("Run Linear Search 🔎", variant="primary")
        
    #displays the list
    list_box = gr.Textbox(label="Random List", lines=2, interactive=False)
    
    #the final result
    result_box = gr.Textbox(label="Final Result", interactive= False)
    
    
    search_steps_box = gr.Textbox(
        label="❓ Did the target match the current iteration? (Search Steps)", 
        lines=5, 
        interactive=False #set to False since it is an output display
    ) 
    
    #connects events
    gen_btn.click(
        fn=generate_list,
        inputs=[],
        outputs=[list_box, arr_state],
    )
    
    run_btn.click(
        fn=linear_search_on_state,
        inputs=[user_number, arr_state],
        outputs= [result_box, search_steps_box], #updated outputs
    )

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Ocean())