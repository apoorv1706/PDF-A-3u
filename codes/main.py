from latexcontent import *
from xmlparser import *
import subprocess


def main():
    xml_parser = XMLParser()
    latex_generator = LatexGenerator()

    xml_file_path = "attachment.xml"
    xsd_file_path = "dcc.xsd"

    # Validation and XML parsing
    validation_result = xml_parser.validate_xml(xml_file_path, xsd_file_path)
    if validation_result:
        latex_content = latex_generator.generate_latex_content()
        # Write LaTeX content to a file or do further processing as needed
        with open("output.tex", "w") as file:
            file.write(latex_content)
    else:
        print("Validation failed. Cannot proceed further.")


    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_pdf = f'CSIR_{current_datetime}.pdf'
    subprocess.run(['pdflatex', '-jobname=' + output_pdf, "output.tex"])


if __name__ == "__main__":
    main()