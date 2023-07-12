# AI Agents talk to each other

This Python script lets you create separate identities for AI agents and let them talk to each other.

You can pick a premade identity list from the `system` folder or you can add your own there in JSON format.

If you like the code, consider [buying me a coffee](https://buymeacoffee.com/unconv)

## Quick start

```console
$ pip install --upgrade openai
$ python3 agent.py
```

## Sample convo

```console
$ ./agent.py

Python Developer: With Python's simplicity, I find no reason to use PHP.

PHP Developer: Combining HTML and PHP in the same file allows me to manipulate page content smoothly, while simple file based routing ensures easier URLs and greater control over web page organization.

Rust Developer: Hi! While Python and PHP have their use-cases, if speed and performance is your priority, Rust might be the language you are looking for. The guarantees of memory safety without a garbage collector makes Rust a first choice for real-time or high-performance applications. I've worked on projects where the switch from Python to Rust led to 10x performance improvement.

Python Developer: Despite Rust's performance, Python's readability and simplicity still make it my first choice.

PHP Developer: I believe PHP's seamless integration with HTML also contributes to its simplicity and makes it my preferred choice for web development tasks.

Rust Developer: Indeed, how easy or difficult a language feels can often depend on the task at hand. Python is a great choice if simplicity and readability are most important, while PHP is really handy when you're mixing server side coding with HTML. Rust, on the other hand, shines when you need the most performance, efficiency and control. It's all about picking the right tool for the job!
```
