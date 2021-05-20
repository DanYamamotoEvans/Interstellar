from argparse import ArgumentParser
from distutils.util import strtobool

def getargs(cmd):
    if cmd=="import":
        argparser = ArgumentParser(usage='%(prog)s import [options]')
        argparser.add_argument('cmdname',help="import")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-R1', '--read1', type=str,default="",help='R1 file')
        argparser.add_argument('-R2', '--read2', type=str,default="",help='R2 file')
        argparser.add_argument('-I1', '--index1', type=str,default="",help='I1 file')
        argparser.add_argument('-I2', '--index2', type=str,default="",help='I2 file')
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')
        argparser.add_argument('-fq_gz', '--input_fastq_gzipped', action="store_true", help='Fastq is gzipped')
        argparser.add_argument('-simple', '--simple', action="store_true", help='Read strucutre is described as non-regular expression format')
        argparser.add_argument('-flash', '--flash',type=str, default="", choices=["","R1-R2","R1-I1","R1-I2","R2-I1","R2-I2","I1-I2"],help='If the paired end reads have overlap, specified reads are merged using flash2 algorithm. exp) R1-R2')
    
    elif cmd=="qc":
        argparser = ArgumentParser(usage='%(prog)s qc [options]')
        argparser.add_argument('cmdname',help="qc")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-rs', '--rawSeq', type=str,required=True,help="gzipped sequence file generated by import")
        argparser.add_argument('-rq', '--rawQual', type=str,required=True,help="gzipped quality file generated by import")
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')

    elif cmd=="to_bt":
        argparser = ArgumentParser(usage='%(prog)s to_bt [options]')
        argparser.add_argument('cmdname',help="to_bt")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-rs', '--rawSeq', type=str,required=True,nargs="*",help="gzipped sequence file generated by import or QC")
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')

    elif cmd=="correct":
        argparser = ArgumentParser(usage='%(prog)s correct [options]')
        argparser.add_argument('cmdname',help="correct")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-ip', '--pickle', type=str,required=True,nargs="*", help='import pickle')
        argparser.add_argument('-no_show_summary', '--no_show_summary', action="store_true",help='Do not show summary on the plot')
        argparser.add_argument('-yscale', '--yaxis_scale', type=str,default="log",choices=["normal","log"],help='yaxis scale for plot')
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')
        
    elif cmd=="mk_sval":
        argparser = ArgumentParser(usage='%(prog)s mk_sval [options]')
        argparser.add_argument('cmdname',help="mk_sval")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-rs', '--rawSeq', type=str,required=True,help="gzipped sequence file generated by import")
        argparser.add_argument('-rq', '--rawQual', type=str,required=True,help="gzipped quality file generated by import")
        argparser.add_argument('-crp', '--correctedPickle', type=str,required=True,help='pickle file generated by correct')
        argparser.add_argument('-resultonly', '--resultonly', action="store_true", help='export only result file (no value files)')
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')

    elif cmd=="buildTree":
        argparser = ArgumentParser(usage='%(prog)s buildTree [options]')
        argparser.add_argument('cmdname',help="buildTree")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-sv', '--srcValue', type=str, required=True, help='source sequence value file generated by correct')
        argparser.add_argument('-samplemerge', '--samplemerge', action="store_true", help='merge multiple samples or not')
        argparser.add_argument('-samplesheet', '--samplesheet', type=str, default="",help='samplesheet if samplemerge==True')
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')

    elif cmd=="mergeTree":
        argparser = ArgumentParser(usage='%(prog)s mergeTree [options]')
        argparser.add_argument('cmdname',help="mergeTree")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-lp', '--localTreePkl', type=str, required=True,nargs='*', help='pickle file of local convert tree')
        argparser.add_argument('-samplemerge', '--samplemerge', action="store_true", help='merge multiple samples or not')
        argparser.add_argument('-samplesheet', '--samplesheet', type=str, default="",help='samplesheet if samplemerge==True')
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')
        return argparser.parse_args()

    elif cmd=="convert":
        argparser = ArgumentParser(usage='%(prog)s convert [options]')
        argparser.add_argument('cmdname',help="convert")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-sv', '--srcValue', type=str, required=True, help='source sequence value file generated by correct')
        argparser.add_argument('-sq', '--srcQuality', type=str, required=True, help='source quality file generated by correct')
        argparser.add_argument('-samplemerge', '--samplemerge', action="store_true", help='merge multiple samples or not')
        argparser.add_argument('-samplesheet', '--samplesheet', type=str, default="",help='samplesheet if samplemerge==True')
        argparser.add_argument('-tree', '--tree', type=str, required=True, help='s-value tree generated in mergeTree')
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')

    elif cmd=="bc_sort":
        argparser = ArgumentParser(usage='%(prog)s bc_sort [options]')
        argparser.add_argument('cmdname',help="bc_sort")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-sseq_to_svalue', '--sseq_to_svalue', type=str,required=True,help="The dictionary of seq to value generagted by 'mk_sval'")
        argparser.add_argument('-tbl', '--table', type=str,required=True,help="tsv file including the correspondence of source and destination")
        argparser.add_argument('-tree', '--tree', type=str, required=True, help='s-value tree generated in mergeTree')
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')

    elif cmd=="export":
        argparser = ArgumentParser(usage='%(prog)s export [options]')
        argparser.add_argument('cmdname',help="export")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-dv', '--destValue', type=str, default="", help='##Required for localConvert and export## pickle file of partially converted components')
        argparser.add_argument('-dq', '--destQual', type=str, default="", help='##Required for localConvert and export## pickle file of partially converted components')
        argparser.add_argument('-rs', '--rawSeq', type=str,required=True,help="gzipped sequence file generated by import")
        argparser.add_argument('-rq', '--rawQual', type=str,required=True,help="gzipped quality file generated by import")
        argparser.add_argument('-size', '--size_info', type=str,required=True,help="capacity information generated by mergeTree")
        argparser.add_argument('-export_bclist', '--export_bclist', action="store_true", help='export the converted barcodes')
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')

    elif cmd=="demultiplex":
        argparser = ArgumentParser(usage='%(prog)s demultiplex [options]')
        argparser.add_argument('cmdname',help="demultiplex")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-cs', '--correctedSeq', type=str,required=True,help="gzipped sequence file generated by import")
        argparser.add_argument('-rq', '--rawQual', type=str,required=True,help="gzipped quality file generated by import")
        argparser.add_argument('-cq', '--correctedQual', type=str,required=True,help="gzipped sequence file generated by import")
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')
        argparser.add_argument('-export_tsv', '--export_tsv', action="store_true", help='export sequence table, not fastq(for demultiplex)')

    elif cmd=="tag":
        argparser = ArgumentParser(usage='%(prog)s tag [options]')
        argparser.add_argument('cmdname',help="tag")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-cs', '--correctedSeq', type=str,required=True,help="gzipped sequence file generated by import")
        argparser.add_argument('-rq', '--rawQual', type=str,required=True,help="gzipped quality file generated by import")
        argparser.add_argument('-cq', '--correctedQual', type=str,required=True,help="gzipped sequence file generated by import")
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='output file name')
        argparser.add_argument('-d', '--outdir', type=str, default=".", help='output directory')

    elif cmd=="streamline":
        argparser = ArgumentParser(usage='%(prog)s streamline [options]')
        argparser.add_argument('cmdname',help="streamline")
        argparser.add_argument('-conf', '--config', type=str,required=True,help="config file")
        argparser.add_argument('-testrun', '--testrun',action="store_true",help="Run with small fractions of input data to check the streamline scripts work.")
        argparser.add_argument('-distribute', '--distribute', action="store_true",help="Execute distributed jobs with qsub")        
        argparser.add_argument('-R1', '--read1', type=str,default="",help='R1 file. See the instruction for import.')
        argparser.add_argument('-R2', '--read2', type=str,default="",help='R2 file. See the instruction for import.')
        argparser.add_argument('-I1', '--index1', type=str,default="",help='I1 file. See the instruction for import.')
        argparser.add_argument('-I2', '--index2', type=str,default="",help='I2 file. See the instruction for import.')
        argparser.add_argument('-fq_gz', '--input_fastq_gzipped', action="store_true", help='Fastq is gzipped. See the instruction for import.')
        argparser.add_argument('-simple', '--simple', action="store_true", help='Read strucutre is described as non-regular expression format. See the instruction for import.')
        argparser.add_argument('-flash', '--flash',type=str, default="", choices=["","R1-R2","R1-I1","R1-I2","R2-I1","R2-I2","I1-I2"],help='If the paired end reads have overlap, specified reads are merged using flash2 algorithm. exp) R1-R2, See the instruction for import.')
        argparser.add_argument('-no_show_summary', '--no_show_summary', action="store_true",help='Do not show summary on the plot. See the instruction for corect.')
        argparser.add_argument('-yscale', '--yaxis_scale', type=str,default="log",choices=["normal","log"],help='yaxis scale for plot. See the instruction for correct.')
        argparser.add_argument('-resultonly', '--resultonly', action="store_true", help='Export only result file (no value files). See the instruction for mk_sval.')
        argparser.add_argument('-samplemerge', '--samplemerge', action="store_true", help='Merge multiple samples or not. See the instruction for buildTree.')
        argparser.add_argument('-samplesheet', '--samplesheet', type=str, default="",help='Samplesheet if samplemerge==True. See the instruction for buildTree.')
        argparser.add_argument('-tbl', '--table', type=str,default="",help="tsv file including the correspondence of source and destination. See the instruction for bc_sort")
        argparser.add_argument('-export_bclist', '--export_bclist', action="store_true", help='Export the converted barcodes')
        argparser.add_argument('-export_tsv', '--export_tsv', action="store_true", help='export sequence table, not fastq. See the instrcution for demultiplex')
        argparser.add_argument('-o', '--outname', type=str,default="dnaSyn",help='Final output file name')
        argparser.add_argument('-d', '--outdir', type=str, required=True, help='Working directory')
        
    return argparser.parse_args()
