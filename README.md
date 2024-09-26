# Setup
This will download Lab 3 locally, allowing you to work on your scripts and upload (push) them back up to GitHub.

1. Clone your lab repository into your ~/ops445/lab3 directory using SSH:
```bash
git clone <ssh link> ~/ops445/lab3/
```
2. Copy your backed-up work into your new GitHub-linked directory:
```bash
cp ~/old_ops445/lab3/* ~/ops445/lab3/
```

# Submission
1. Run the checking script. Make sure you identify and correct any and all errors in your scripts:
```bash
cd ~/ops445/lab3/
pwd #confirm that you are in the right directory
python3 ./CheckLab3.py -f -v
```
2. Redirect the checking script output into *laboutput.txt*:
```bash
python3 ./CheckLab3.py -f -v &> ~/ops445/lab3/laboutput.txt
```

In addition to the files you started with, your repository should include the
following files you have created:

- [ ] lab3a.py
- [ ] lab3b.py
- [ ] lab3c.py
- [ ] lab3d.py
- [ ] lab3e.py
- [ ] lab3f.py
- [ ] laboutput.txt 

3. Commit and push (upload) your lab work:
```bash
git add lab*
git commit -m "Individual message or note."
git push
```

You can make changes to your scripts and reupload as many times as you like. Make sure you commit+push to do so.

**Note:** Your lab is automatically submitted at the due date and time using the last published code. Any changes you publish after the due date won't be marked or seen by your professor.
