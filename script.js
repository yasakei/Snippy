document.addEventListener('DOMContentLoaded', function () {
    // --- Terminal Animation ---
    const terminalBody = document.getElementById('terminal-body');
    const steps = [
        { type: 'command', text: 'snippy save my-ip "curl ifconfig.me"' },
        { type: 'output', text: "Snippet 'my-ip' saved." },
        { type: 'command', text: 'snippy list' },
        { type: 'output', text: 'my-ip: curl ifconfig.me' },
        { type: 'command', text: 'snippy run my-ip' },
        { type: 'output', text: '123.45.67.89' },
        { type: 'command', text: 'snippy delete my-ip' },
        { type: 'output', text: "Snippet 'my-ip' deleted." },
    ];

    let stepIndex = 0;

    const processNextStep = () => {
        if (stepIndex >= steps.length) {
            setTimeout(() => {
                terminalBody.innerHTML = '';
                stepIndex = 0;
                processNextStep();
            }, 3000); // Pause before looping
            return;
        }

        const step = steps[stepIndex];
        const line = document.createElement('div');

        if (step.type === 'command') {
            line.classList.add('terminal-line');
            line.innerHTML = `<span class="prompt-prefix">$ </span><span id="typed-${stepIndex}"></span>`;
            terminalBody.appendChild(line);
            
            new Typed(`#typed-${stepIndex}`, {
                strings: [step.text],
                typeSpeed: 40,
                showCursor: true,
                cursorChar: '█',
                onComplete: (self) => {
                    self.cursor.remove(); // Remove cursor on complete
                    stepIndex++;
                    setTimeout(processNextStep, 500);
                }
            });
        } else { // 'output'
            line.classList.add('command-output');
            line.textContent = step.text;
            terminalBody.appendChild(line);
            terminalBody.scrollTop = terminalBody.scrollHeight;
            stepIndex++;
            setTimeout(processNextStep, 1200);
        }
    };

    processNextStep(); // Start the animation

    // --- Copy Button ---
    const copyButton = document.getElementById('copy-button');
    const installCommandText = document.querySelector('.install-box code').innerText;

    copyButton.addEventListener('click', () => {
        navigator.clipboard.writeText(installCommandText).then(() => {
            const originalIcon = copyButton.innerHTML;
            copyButton.innerHTML = '<i class="fas fa-check"></i>';
            copyButton.title = 'Copied!';
            
            setTimeout(() => {
                copyButton.innerHTML = originalIcon;
                copyButton.title = 'Copy to clipboard';
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy text: ', err);
        });
    });
});