import subprocess

def execute_command(cmd: str):
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()
    return {"stdout": stdout, "stderr": stderr, "exit_code": process.returncode}